from snake import scale
import numpy as np
import base64
import math
import cv2


class Commands(scale.Commands):
    def check(self):
        pass

    @scale.command({
        'info': 'create bitmap image from the file passed'
    })
    def bitmap(self, args, file, opts):
        width = 64
        resize = 3
        binary = np.fromfile(file.file_path, dtype='uint8')
        length = len(binary)
        height = math.ceil(length / width)
        reshaped = np.resize(binary,(height, width))
        dimension = (width * resize, height * resize)
        resized = cv2.resize(reshaped, dimension, interpolation = cv2.INTER_AREA)
        image = cv2.imencode('.png', resized)
        b64bytes = base64.b64encode(image[1])
        b64str = b64bytes.decode('utf-8')
        return {'bitmap': b64str}

    def bitmap_markdown(self, json):
        output = ('![Bitmap](data:image/png;base64,' + json['bitmap'] + ')')
        return output
