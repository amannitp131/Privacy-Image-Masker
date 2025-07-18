# Info Detector - Privacy Image Masker

A comprehensive privacy protection tool that automatically detects and masks sensitive information in images using advanced AI technologies. This project combines computer vision, OCR (Optical Character Recognition), and Natural Language Processing to identify and redact Personally Identifiable Information (PII) from uploaded images.

## 🌟 Features

- **Automatic PII Detection**: Detects various types of sensitive information including:
  - Aadhaar numbers (Indian national ID)
  - PAN card numbers
  - Phone numbers
  - Email addresses
  - Names and personal information
  - Dates and other temporal data

- **Advanced AI Technologies**:
  - YOLO v8 for object detection
  - EasyOCR for text extraction from images
  - spaCy for natural language processing
  - Computer vision techniques for precise masking

- **User-Friendly Interface**: Modern, responsive web interface built with Next.js and Tailwind CSS

- **Real-time Processing**: Fast image processing with immediate visual feedback

- **Cross-Platform Support**: Works on Windows, macOS, and Linux

## 🏗️ Architecture

The project consists of three main components:

### 1. Frontend (Next.js)
- **Location**: `detector/`
- **Technology**: Next.js 15.4.1, React 19.1.0, Tailwind CSS 4
- **Purpose**: User interface for image upload and display of masked results

### 2. Backend (Express.js)
- **Location**: `Backend/`
- **Technology**: Node.js, Express.js, Multer
- **Purpose**: API gateway that handles file uploads and communicates with the AI service

### 3. AI Service (FastAPI)
- **Location**: `Service/`
- **Technology**: Python, FastAPI, OpenCV, EasyOCR, spaCy, YOLO v8
- **Purpose**: Core image processing and PII detection engine

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **pip** (Python package manager)
- **npm** or **yarn**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/amannitp131/Info_Detector.git
   cd Info_Detector
   ```

2. **Set up the AI Service**
   ```bash
   cd Service
   pip install fastapi uvicorn opencv-python easyocr spacy ultralytics numpy pillow python-multipart
   python -m spacy download en_core_web_sm
   ```

3. **Set up the Backend**
   ```bash
   cd ../Backend
   npm install
   ```

4. **Set up the Frontend**
   ```bash
   cd ../detector
   npm install
   ```

### Running the Application

Start all three services in separate terminals:

1. **Start the AI Service** (Port 8001)
   ```bash
   cd Service
   uvicorn main:app --host 0.0.0.0 --port 8001
   ```

2. **Start the Backend** (Port 3001)
   ```bash
   cd Backend
   node index.js
   ```

3. **Start the Frontend** (Port 3000)
   ```bash
   cd detector
   npm run dev
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:3000`

## 📝 Usage

1. **Upload an Image**: Click the "Upload Image" button and select an image containing text
2. **Processing**: The system will automatically:
   - Extract text using OCR
   - Analyze the text for PII using NLP
   - Detect objects and text regions using YOLO
   - Apply masking to sensitive areas
3. **Download Result**: View and download the masked image with PII redacted

## 🔧 Configuration

### Environment Variables

Create `.env` files in each component directory:

**Backend/.env**
```env
PORT=3001
AI_SERVICE_URL=http://127.0.0.1:8001
```

**Service/.env**
```env
PORT=8001
MODEL_PATH=./yolov8n.pt
```

### Model Configuration

The AI service uses YOLOv8 nano model (`yolov8n.pt`) for object detection. You can replace this with other YOLO models for better accuracy:
- `yolov8s.pt` (small)
- `yolov8m.pt` (medium)
- `yolov8l.pt` (large)
- `yolov8x.pt` (extra large)

## 🧪 API Documentation

### Backend API

**POST** `/mask`
- **Description**: Upload an image for PII masking
- **Content-Type**: `multipart/form-data`
- **Parameters**: 
  - `image`: Image file (JPEG, PNG, etc.)
- **Response**: Masked image as binary stream

### AI Service API

**POST** `/process`
- **Description**: Process image for PII detection and masking
- **Content-Type**: `multipart/form-data`
- **Parameters**: 
  - `file`: Image file
- **Response**: Processed image with masked PII

## 🛡️ Privacy & Security

- **Local Processing**: All image processing happens locally on your machine
- **No Data Storage**: Images are temporarily stored only during processing
- **Automatic Cleanup**: Uploaded files are automatically removed after processing
- **No External APIs**: No data is sent to external services

## 🧰 Technologies Used

### Frontend
- Next.js 15.4.1
- React 19.1.0
- Tailwind CSS 4
- Axios for HTTP requests

### Backend
- Express.js 5.1.0
- Multer for file uploads
- CORS for cross-origin requests
- Axios for service communication

### AI Service
- FastAPI for API framework
- OpenCV for image processing
- EasyOCR for text extraction
- spaCy for NLP
- YOLO v8 for object detection
- NumPy for numerical operations

## 📁 Project Structure

```
Info_Detector/
├── README.md
├── .gitignore
├── Backend/
│   ├── index.js           # Express server
│   ├── package.json       # Node.js dependencies
│   └── uploads/           # Temporary file storage
├── detector/
│   ├── src/
│   │   └── app/
│   │       ├── page.js    # Main React component
│   │       ├── layout.js  # App layout
│   │       └── globals.css # Global styles
│   ├── package.json       # Next.js dependencies
│   ├── next.config.mjs    # Next.js configuration
│   └── tailwind.config.js # Tailwind configuration
└── Service/
    ├── main.py           # FastAPI application
    ├── yolov8n.pt       # YOLO model weights
    └── __pycache__/     # Python cache files
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the ISC License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] Support for more PII types (credit cards, social security numbers)
- [ ] Batch processing for multiple images
- [ ] Custom masking styles (blur, pixelate, black boxes)
- [ ] API rate limiting and authentication
- [ ] Docker containerization
- [ ] Performance optimizations
- [ ] Support for video processing
- [ ] Custom model training interface

## 📞 Support

For support, email amanmis601@gmail.com or create an issue in the GitHub repository.

## 🙏 Acknowledgments

- YOLO v8 by Ultralytics
- EasyOCR by JaidedAI
- spaCy by Explosion AI
- Next.js by Vercel
- FastAPI by Sebastián Ramirez

---
