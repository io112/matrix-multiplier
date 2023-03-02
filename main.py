import json
import logging
from typing import List

import numpy as np
import pydantic
from pydantic import BaseModel

logging.basicConfig(format="")


class Request(BaseModel):
    A: List[List[int]]
    B: List[List[int]]


class Response(BaseModel):
    output: List[List[int]]


def main():
    with open('request.json', 'r') as f:
        try:
            data = Request(**json.loads(f.read()))
        except json.JSONDecodeError as err:
            logging.error('Unable to deserialize request: ', exc_info=err)
            return
        except pydantic.ValidationError as err:
            logging.error('Bad request format: ', exc_info=err)
            return

    a = np.array(data.A)
    b = np.array(data.B)
    res = Response(output=a.dot(b).tolist())
    with open('response.json', 'w') as f:
        f.write(res.json())


if __name__ == '__main__':
    main()
