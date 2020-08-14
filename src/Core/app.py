from flask import Flask
import os

# local
from config import Configurations

app = Flask(
    __name__,
    template_folder=os.path.abspath('../templates'),
    static_folder=os.path.abspath('../static'),
)
app.config.from_object(Configurations)


