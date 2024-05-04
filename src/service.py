# python
import io
import json
import logging

# 3rdparty
import cv2
import pydantic
import numpy as np

from fastapi import FastAPI, File, UploadFile, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from PIL import Image

# project
from src.datacontract.service_config import ServiceConfig
from src.datacontract.service_output import ServiceOutput
from src.photoopen import get_boxes
from ultralytics import YOLO
from norfair import Tracker
from norfair.camera_motion import MotionEstimator

from deep_sort_realtime.deepsort_tracker import DeepSort
from ultralytics import YOLO

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

app = FastAPI()
tracker = DeepSort(max_age=50)
model = YOLO('src/best.pt')

model = YOLO('src/best.pt')

tracker = Tracker(
distance_function="frobenius",
distance_threshold=200,
)

motion_estimator = MotionEstimator()

service_config_path = ".\\src\\configs\\service_config.json"
with open(service_config_path, "r") as service_config:
    service_config_json = json.load(service_config)

service_config_adapter = pydantic.TypeAdapter(ServiceConfig)
service_config_python = service_config_adapter.validate_python(service_config_json)

logger.info(f"Загружена конфигурация сервиса по пути: {service_config_path}")


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def health_check() -> str:
    """Точка доступа для проверки жизни сервиса

    Возрващает:
        * HTTP Статус код (ОК)
    """
    return '{"Status" : "OK"}'


@app.post("/file/")
async def inference(image: UploadFile = File(...)) -> JSONResponse:
    """Метод для преобразования изображения, а именно ресайза

    Параметры:
        * `image` (`UploadFile`, `optional`): объект изображения

    Возвращает:
        * `JSONResponse`: JSON-ответ с информацией о координатах рамок и классах объектов
    """
    image_content = await image.read()
    cv_image = np.array(Image.open(io.BytesIO(image_content)))
    logger.info(f"Картиночка приянята... обрабатываю...")
    

    try:
<<<<<<< Updated upstream
        labels = get_boxes(cv_image, model, tracker, motion_estimator)
=======
        labels = get_boxes(cv_image, model, tracker)
>>>>>>> Stashed changes
        
        service_output_json = list()
        
        
        
        for label in labels:     
            
            service_output = ServiceOutput()
            service_output.x1 = label[1]
            service_output.y1 = label[2]
            service_output.x2 = label[3]
            service_output.y2 = label[4]
            service_output.classe = label[0]
            service_output.id = label[5]
            
            service_output_json.append(service_output.model_dump(mode="json"))
            
        return JSONResponse(content=jsonable_encoder(service_output_json))
    
    except Exception as e:
        logger.warning(e)