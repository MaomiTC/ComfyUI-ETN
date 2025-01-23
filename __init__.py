from .ETN_LoadMaskBase64 import ETN_LoadMaskBase64
from .image_websocket_node import ImageWebSocketOutput

NODE_CLASS_MAPPINGS = {
    "ETN_LoadMaskBase64": ETN_LoadMaskBase64,
    "ImageWebSocketOutput": ImageWebSocketOutput
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ETN_LoadMaskBase64": "Load Mask (Base64)",
    "ImageWebSocketOutput": "Image WebSocket Output"
}

NODE_CATEGORY_MAPPINGS = {
    "ETN_LoadMaskBase64": "ETN Nodes",
    "ImageWebSocketOutput": "ETN Nodes"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'NODE_CATEGORY_MAPPINGS'] 