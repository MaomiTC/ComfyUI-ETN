import websockets
import asyncio
import json
import base64
from PIL import Image
import io
import numpy as np
import torch
import time

class ImageWebSocketOutput:
    def __init__(self):
        self.websocket = None
        self.server_url = "ws://localhost:3001"
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "prompt": ("STRING", {"default": ""})
            }
        }
    
    RETURN_TYPES = ()
    FUNCTION = "send_image"
    OUTPUT_NODE = True
    CATEGORY = "ETN Nodes"

    async def send_ws_message(self, image_data, prompt):
        try:
            async with websockets.connect(self.server_url) as websocket:
                message = {
                    "type": "image",
                    "image": image_data,
                    "prompt": prompt,
                    "timestamp": int(time.time() * 1000)
                }
                await websocket.send(json.dumps(message))
                print(f"Image sent successfully with prompt: {prompt}")
        except Exception as e:
            print(f"WebSocket发送错误: {str(e)}")
            import traceback
            print(traceback.format_exc())

    def send_image(self, images, prompt):
        try:
            # 转换图像格式
            image = images[0]
            
            # 确保图像是numpy数组
            if isinstance(image, torch.Tensor):
                image = image.cpu().numpy()
                
            # 确保值在0-255范围内
            if image.max() <= 1.0:
                image = (image * 255).astype(np.uint8)
            else:
                image = image.astype(np.uint8)
                
            # 转换为PIL图像
            pil_image = Image.fromarray(image)
            
            # 转换为base64
            buffer = io.BytesIO()
            pil_image.save(buffer, format="PNG")
            image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            # 发送数据
            asyncio.run(self.send_ws_message(image_data, prompt))
            print("Image processed and sent via WebSocket")
            
        except Exception as e:
            print(f"Error in send_image: {str(e)}")
            import traceback
            print(traceback.format_exc())
            
        return ()

NODE_CLASS_MAPPINGS = {
    "ImageWebSocketOutput": ImageWebSocketOutput
} 