# Two-Wheeler Surveillance System

This Python project implements a surveillance system designed to detect and analyze traffic violations related to two-wheeler transports. The system focuses on identifying instances of triple riding and no helmet violations.

## Features

### Triple Riding Detection

The surveillance system uses computer vision techniques to detect instances of triple riding on two-wheeler vehicles. It can analyze video feeds or images to identify violations where three individuals are riding on a single two-wheeler.

### No Helmet Violation Detection

The system is equipped to recognize violations where riders on two-wheelers are not wearing helmets. It employs image processing algorithms to detect the absence of helmets on riders.

## Technologies Used

- **Python:** Core programming language for the project.
- **Computer Vision Libraries:** OpenCV, TensorFlow, or other relevant libraries for image and video analysis.
- **Machine Learning (Optional):** ML models can be integrated for improved detection accuracy.
- **Data Storage (Optional):** Utilize databases to store violation records and relevant information.

## Getting Started

Follow these steps to set up and run the Two-Wheeler Surveillance System:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/pks916/traffic_violation_detection_system.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd traffic_violation_detection_system
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Surveillance System:**
    ```bash
    python src/main.py
    ```

## Usage

1. Provide input data: Video feed
2. Run the surveillance system to analyze the input data.
3. View the output, which includes identified violations and relevant information.

## Contributing

Contributions to enhance the accuracy, efficiency, or additional features of the surveillance system are welcome. Before contributing, please review the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The project may utilize pre-trained models or algorithms from the open-source community. Credits and acknowledgments are provided in the relevant sections of the code or documentation.


