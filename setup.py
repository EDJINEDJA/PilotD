import argparse
from time import sleep, time
import yaml
from db.preprocessing import PreProcessing

parser = argparse.ArgumentParser()
parser.add_argument("--config" , type=str  , required=True , help="path to yaml config")
args = parser.parse_args()

with open(args.config , mode="r") as stream:
        config = yaml.safe_load(stream)

parser = PreProcessing(config)
parser.Loading()
sleep(1)
parser.Build()
#parser.Test()