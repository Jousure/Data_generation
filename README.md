# 🚀 Genify - Advanced Data Generation Platform

**🚧 Work in Progress - Currently Under Development 🚧**

**Genify** is a powerful and scalable data generation platform that creates realistic mock datasets for testing, development, and data science applications. Built with a modern React frontend and FastAPI backend, supporting 15+ data types and capable of generating up to 100,000+ records.

## ✨ Features

### 🎯 Core Capabilities
- **📊 Massive Scale**: Generate datasets from 1 to 100,000+ records
- **🎨 Modern UI**: Beautiful, responsive interface with dark/light theme support
- **⚡ Real-time Preview**: See your data before generating the full dataset
- **🔧 Advanced Schema Generation**: AI-powered schema creation from natural language descriptions
- **📱 Mobile Responsive**: Works seamlessly on all device sizes

### 📋 Supported Data Types

📖 **[View Complete Data Types Reference](./frontend/DATA_TYPES.md)** - Comprehensive guide to all 15+ available data generation categories including:

- Location & Address Data
- Person & Demographics  
- Business & Finance
- Technology & Digital
- Healthcare & Medical
- Automotive
- Construction
- Entertainment & Media
- Food & Grocery
- Products & Retail
- Identification Numbers
- Aviation
- Education
- Professional Skills
- Nature & Biology
- Data & Programming
- Text & Content
- Statistical Distributions
- Dates & Times

## 🏗️ Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **Data Generation**: Faker, NumPy, Custom algorithms
- **Validation**: Pydantic models
- **File Operations**: CSV export with configurable options

### Frontend (React)
- **Framework**: React 19 with Vite
- **Styling**: Tailwind CSS 4.x
- **State Management**: React hooks and context
- **UI Components**: Custom component library

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 18+
- npm or yarn

### Installation

1. **Clone the Genify repository**
   ```bash
git clone https://github.com/Jousure/Genify.git
cd Genify
```

2. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

1. **Start the Backend Server**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the Frontend Development Server**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 📖 Usage

### Basic Data Generation
1. Describe your dataset in natural language (e.g., "Generate customer data with names, emails, and phone numbers")
2. Set the number of records you want to generate
3. Preview the generated data
4. Download as CSV

### Advanced Features
- **Custom Schemas**: Define specific column types and constraints
- **Data Validation**: Ensure generated data meets your requirements
- **Batch Generation**: Generate multiple datasets in parallel
- **Export Options**: Multiple formats (CSV, JSON, Excel coming soon)

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the backend directory:

```env
# Optional: OpenAI API key for enhanced schema generation
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Custom data generation settings
MAX_RECORDS_PER_REQUEST=100000
DEFAULT_OUTPUT_FORMAT=csv
```

## 📚 API Documentation

### Main Endpoints

#### Generate Data
```http
POST /api/generate
Content-Type: application/json

{
  "description": "Generate customer data with names and emails",
  "num_records": 1000,
  "schema": null  // Optional custom schema
}
```

#### Get Available Data Types
```http
GET /api/data-types
```

#### Preview Data
```http
POST /api/preview
Content-Type: application/json

{
  "description": "Generate customer data",
  "num_records": 5
}
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🤝 Contributing

**🚧 This project is currently under active development 🚧**

**Genify** welcomes contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- **New Data Types**: Add support for additional data generation patterns
- **UI/UX Improvements**: Enhance the user interface and experience
- **Performance**: Optimize data generation for larger datasets
- **Export Formats**: Add support for JSON, Excel, Parquet formats
- **Validation**: Improve data validation and schema enforcement
- **Documentation**: Help improve documentation and examples

## 🗺️ Roadmap

### ✅ Completed
- [x] Basic data generation with 15+ data types
- [x] Modern React UI with Tailwind CSS
- [x] Real-time preview functionality
- [x] CSV export capability
- [x] Dark/light theme support
- [x] Scalable generation up to 100,000+ records
- [x] AI-powered schema generation

### 🚧 In Progress
- [ ] User authentication and profiles
- [ ] Saved dataset templates
- [ ] Advanced filtering and search
- [ ] Data validation rules
- [ ] Batch operations

### 📋 Planned
- [ ] Additional export formats (JSON, Excel, Parquet)
- [ ] Data relationship generation
- [ ] API rate limiting and quotas
- [ ] Docker containerization
- [ ] Cloud deployment options
- [ ] Advanced analytics and reporting
- [ ] Data privacy and GDPR compliance
- [ ] Enterprise features and SSO

## 🐛 Known Issues

- Large dataset generation (>50,000 records) may take several minutes
- Memory usage increases significantly with very large datasets
- Some complex data types may need additional validation
- UI responsiveness during large generation operations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Faker](https://github.com/joke2k/faker) - Excellent fake data generation library
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [React](https://reactjs.org/) - JavaScript library for building user interfaces
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Vite](https://vitejs.dev/) - Next generation frontend tooling

## 📞 Support

For questions, suggestions, or issues about **Genify**:
- Create an issue on GitHub
- Check the [documentation](frontend/DATA_TYPES.md) for available data types
- Review the API docs at `/docs` when running the backend

## 🎉 About Genify

**Genify** simplifies the process of creating realistic test data for developers, QA engineers, and data scientists. Whether you need customer data, financial records, healthcare information, or any other type of structured data, Genify provides an intuitive interface and powerful backend to generate exactly what you need.

---

**⚠️ Disclaimer**: This is a development version. Features may change, and some functionality may be incomplete. Use at your own risk for production workloads.
