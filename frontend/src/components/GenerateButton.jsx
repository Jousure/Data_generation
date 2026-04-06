import { generateCSV } from "../api/backend";
import { useState } from "react";

export default function GenerateButton({ columns, rows, darkMode }) {
  const [loading, setLoading] = useState(false);
  
  async function handle() {
    if (loading) return;
    
    setLoading(true);
    try {
      const res = await generateCSV(columns, rows);
      
      // Create download link
      const link = document.createElement('a');
      link.href = `http://127.0.0.1:8000/${res.file}`;
      link.download = res.file.split('/').pop();
      link.style.display = 'none';
      
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      
    } catch (error) {
      alert(`Error generating CSV: ${error.message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <button
      onClick={handle}
      disabled={loading || columns.length === 0}
      className="btn btn-primary w-full"
    >
      {loading ? (
        <>
          <svg className="animate-spin w-4 h-4" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
          </svg>
          <span>Generating {rows.toLocaleString()} rows...</span>
        </>
      ) : (
        <>
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 011.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clipRule="evenodd" />
          </svg>
          <span>Download CSV</span>
        </>
      )}
    </button>
  );
}
