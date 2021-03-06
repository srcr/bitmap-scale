# bitmap-scale
Snake scale to create bitmap images of malware samples

![Screenshot](https://github.com/srcr/bitmap-scale/raw/master/example/bitmap-scale.png "Screenshot of the bitmap-scale analysis")


## Installation

This scale can be installed in two way, pip or by cloning the respository and pointing Snake to it.

Once installed Snake and the Celery workers must be restarted.

This is scale is depending on 2 python modules :
* OpenCV
* base64
* Numpy
* math

> Note: Any missing dependencies will be reported in Snake's log!

### Pip Based

A scale can be installed using pip as follows:

```bash
# 1. Install the scale with pip
pip install git+https://github.com/srcr/bitmap-scale

# 2. Install system dependencies
# If any, these will be reported in the Snake log, or usually listed in the `check` functions within components
```

### Clone Based

All the scales from a repository can easily be added to Snake, just by cloning and pointing.

```bash
# 1. Clone the repository to the desired location
git clone https://github.com/srcr/bitmap-scale.git <SCALE_DIR>

# 2. Add directory to snake.conf
[snip]
snake_scale_dirs: [ '<SCALE_DIR>' ]
[snip]

# 3. Install python requirements
# If any, either look through the setup.py files or look at the Snake log.

# 4. Install system dependencies
# If any, these will be reported in the Snake log, or usually listed in the `check` functions within components
```
