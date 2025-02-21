from adapter.controller.UserController import UserController
from infraestructure.UserRepository import UserRepository
#import dotenv
#from dotenv import load_dotenv
import uvicorn
import logging
import os
from fastapi import FastAPI

class Program:
    app: FastAPI
    logger: logging.Logger

    def __init__(self) -> None:
        #load_dotenv()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing program")
        self.app = FastAPI(
            title="Mi primera API",
            description="Mi primera API utlizando arquitectura limpia",
            docs_url="/swagger",
        )
        print(os.getenv("CONN"))
        UserRepository.setConnectionString(os.getenv("CONN"))
        UserController(self.app)
        self.logger.info("Program initialized")

program = Program()


if __name__ == "__main__":
    uvicorn.run("Program:program.app", host="0.0.0.0", port=8000, reload=True)