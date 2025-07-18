# OBS Switch Controller Integration

This project integrates OBS Studio with Nintendo Switch controller inputs via Kafka messaging. It allows for automated control of both OBS scenes/recording and Nintendo Switch controller inputs based on events received through Kafka.

## Components

- **OBS Controller**: Connects to OBS Studio via WebSocket protocol to control scenes and recording.
- **Switch Controller**: Connects to NXBT webapp to send controller inputs to Nintendo Switch.
- **Kafka Integration**: Uses Kafka to receive events that trigger actions on either OBS or Switch controller.
- **Runner**: Coordinates between all components, listening for Kafka messages and executing appropriate actions.

## Requirements

- Python 3.8+
- OBS Studio with WebSocket plugin (v4.9.0+)
- NXBT webapp running (for Nintendo Switch controller emulation)
- Kafka server running

## Installation

### From Source

1. Clone the repository
2. Install the package in development mode:

```bash
pip install -e .
```

### Using pip

```bash
pip install obs-switch
```

## Usage

### Running the Integration

Start the runner with default settings:

```bash
obs-switch
```

Or customize the connection parameters:

```bash
obs-switch --obs-host localhost --obs-port 4455 --switch-url http://localhost:8000 --kafka-topics spl_replay_service
```

### Running from Source

If you've installed the package in development mode, you can also run it directly:

```bash
python -m obs_switch.cli
```

### Kafka Message Format

The runner listens for Kafka messages in the following formats:

#### Change OBS Scene

```json
{
  "event_type": "obs_scene_change",
  "scene_name": "Scene Name"
}
```

#### Control OBS Recording

```json
{
  "event_type": "obs_recording",
  "action": "start|stop|toggle"
}
```

#### Press Switch Buttons

```json
{
  "event_type": "switch_button",
  "buttons": ["A", "B", "X", "Y"],
  "delay": 0.1
}
```

#### Move Switch Stick

```json
{
  "event_type": "switch_stick",
  "stick": "L_STICK",
  "x_value": 100,
  "y_value": 0,
  "delay": 0.1
}
```

#### Enter Replay Code

```json
{
  "event_type": "switch_replay_code",
  "code": "1234-5678-9012"
}
```

## Architecture

The system uses a modular architecture with the following components:

1. **OBS Controller** (`obs_controller.py`): Handles communication with OBS Studio via WebSocket.
2. **Switch Controller** (`switch_controller.py`): Manages Nintendo Switch controller inputs via NXBT.
3. **Kafka Consumer** (`async_consumer.py`): Listens for events from Kafka topics.
4. **Switch Handler** (`switch_handler.py`): Processes complex Switch input sequences like replay codes.
5. **Runner** (`runner.py`): Coordinates all components and processes incoming Kafka messages.

## Development

### Adding New Event Types

To add support for new event types:

1. Modify the `_process_kafka_message` method in `runner.py`
2. Add a new condition for your event type
3. Implement the corresponding action logic

### Extending Controller Functionality

To add new controller actions:

1. Implement the new functionality in the appropriate controller class
2. Update the runner to expose the new functionality via Kafka messages

## Troubleshooting

- Ensure OBS Studio is running with the WebSocket plugin enabled
- Verify the NXBT webapp is running and accessible
- Check that Kafka server is running and the topics exist
- Review logs for connection errors or message processing issues

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.