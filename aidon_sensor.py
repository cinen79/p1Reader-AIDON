# aidon_sensor.py

from esphome import config_validation as cv
from esphome.components import uart, sensor
from esphome.core import ESPHomeCore
from esphome import automation

# Define the schema for the configuration
CONF_AIDON_SENSOR = 'aidon_sensor'

# Create a schema to validate the user configuration
aidon_sensor_schema = cv.Schema({
    cv.Required(CONF_AIDON_SENSOR): cv.positive_int,  # Assume the user provides polling interval
}).extend(uart.UART_SCHEMA)

# The function that generates the C++ code for the component
def to_code(config):
    uart_ = yield uart.get_uart_interface(config)  # Get UART interface from the YAML config
    poll_interval = config[CONF_AIDON_SENSOR]
    
    # Create the C++ object (AidonSensor) and pass it to the code generator
    return AidonSensor(uart_, poll_interval)
