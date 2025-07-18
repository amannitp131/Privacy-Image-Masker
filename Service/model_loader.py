import torch
from ultralytics import YOLO
import warnings

def load_yolo_model(model_path="yolov8n.pt"):
    """
    Load YOLO model with fallback options for PyTorch 2.6+ compatibility
    """
    try:
        
        model = YOLO(model_path)
        return model
    except Exception as e:
        print(f"Standard YOLO loading failed: {e}")
        
        try:
            
            import torch._C
            original_load = torch.load
            
            def patched_load(*args, **kwargs):
                kwargs['weights_only'] = False
                return original_load(*args, **kwargs)
            
            torch.load = patched_load
            model = YOLO(model_path)
            torch.load = original_load  
            return model
            
        except Exception as e2:
            print(f"Patched YOLO loading also failed: {e2}")
            print("YOLO model will not be available. Continuing with OCR-only processing.")
            return None

def safe_yolo_predict(model, image):
    """
    Safely run YOLO prediction with error handling
    """
    if model is None:
        return None
    
    try:
        return model(image)
    except Exception as e:
        print(f"YOLO prediction failed: {e}")
        return None
