import { useState, useEffect } from "react";
import TopicInput from "./components/TopicInput";
import ColumnEditor from "./components/ColumnEditor";
import PreviewTable from "./components/PreviewTable";
import GenerateButton from "./components/GenerateButton";
import RowSelector from "./components/RowSelector";
import DarkModeToggle from "./components/DarkModeToggle";
import DataTypesReference from "./components/DataTypesReference";
import { getSchema, getPreview } from "./api/backend";

export default function App() {
  const [topic, setTopic] = useState("");
  const [columns, setColumns] = useState([]);
  const [rows, setRows] = useState(100);
  const [preview, setPreview] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [darkMode, setDarkMode] = useState(() => {
    // Check localStorage for saved preference first
    const saved = localStorage.getItem('theme-preference');
    if (saved !== null) return saved === 'dark';
    
    // Fallback to system preference
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  });

  useEffect(() => {
    // Apply theme to document
    const root = document.documentElement;
    if (darkMode) {
      root.classList.add('dark');
      root.setAttribute('data-theme', 'dark');
    } else {
      root.classList.remove('dark');
      root.setAttribute('data-theme', 'light');
    }
    
    // Save preference to localStorage with timestamp
    localStorage.setItem('theme-preference', darkMode ? 'dark' : 'light');
    localStorage.setItem('theme-timestamp', Date.now().toString());
  }, [darkMode]);

  // Listen for system theme changes
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const handleChange = (e) => {
      // Only change if user hasn't explicitly set a preference
      if (!localStorage.getItem('theme-preference')) {
        setDarkMode(e.matches);
      }
    };
    
    mediaQuery.addEventListener('change', handleChange);
    return () => mediaQuery.removeEventListener('change', handleChange);
  }, []);

  async function handleSchema() {
    if (!topic.trim()) {
      setError("Please describe the dataset you want to generate");
      return;
    }
    
    setLoading(true);
    setError("");
    
    try {
      const res = await getSchema(topic);
      setColumns(res.columns);
      setPreview([]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function handlePreview() {
    if (columns.length === 0) {
      setError("Please generate a schema first");
      return;
    }
    
    setLoading(true);
    setError("");
    try {
      const res = await getPreview(columns);
      setPreview(res.preview);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-theme text-theme font-sans antialiased theme-transition">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <header className="mb-8 animate-fadeIn">
          <div className="card card-hover animate-slideUp">
            <div className="p-6 sm:p-8">
              <div className="flex justify-between items-start sm:items-center gap-4">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-3">
                    <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-theme-accent1 to-theme-accent2 flex items-center justify-center hover-lift">
                      <svg className="w-7 h-7 text-white" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z" />
                      </svg>
                    </div>
                    <div>
                      <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-theme mb-2">
                        Dataset Generator
                      </h1>
                      <p className="text-theme opacity-80 text-lg">
                        Professional data generation with realistic, context-aware datasets
                      </p>
                    </div>
                  </div>
                </div>
                <DarkModeToggle darkMode={darkMode} setDarkMode={setDarkMode} />
              </div>
            </div>
          </div>
        </header>

        {/* Error Alert */}
        {error && (
          <div className="mb-6 p-4 rounded-xl border flex items-start gap-3 animate-slideUp card bg-red-50 border-red-200 text-red-800 dark:bg-red-900/20 dark:border-red-800 dark:text-red-300">
            <svg className="w-5 h-5 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
            </svg>
            <div>
              <p className="font-medium">Error</p>
              <p className="text-sm opacity-90">{error}</p>
            </div>
          </div>
        )}

        {/* Main Content Grid */}
        <div className="grid lg:grid-cols-3 gap-6 lg:gap-8">
          {/* Left Column - Input & Controls */}
          <div className="lg:col-span-1 space-y-6">
            {/* Topic Input */}
            <section className="card card-hover animate-slideUp">
              <div className="p-6">
                <h2 className="text-lg font-semibold mb-4 flex items-center gap-2 text-theme">
                  <svg className="w-5 h-5 text-accent1" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                  </svg>
                  Dataset Description
                </h2>
                <TopicInput topic={topic} setTopic={setTopic} onSubmit={handleSchema} darkMode={darkMode} />
              </div>
            </section>

            {/* Schema Controls */}
            {columns.length > 0 && (
              <section className="card card-hover animate-slideUp">
                <div className="p-6">
                  <h2 className="text-lg font-semibold mb-4 flex items-center gap-2 text-theme">
                    <svg className="w-5 h-5 text-accent1" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zM3 10a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6zM14 9a1 1 0 00-1 1v6a1 1 0 001 1h2a1 1 0 001-1v-6a1 1 0 00-1-1h-2z" />
                    </svg>
                    Schema Columns
                    <span className="ml-2 text-xs px-2 py-1 rounded-full bg-accent1 text-white">
                      {columns.length}
                    </span>
                  </h2>
                  <ColumnEditor columns={columns} setColumns={setColumns} darkMode={darkMode} />
                  
                  <div className="space-y-3 mt-6">
                    <button
                      onClick={handlePreview}
                      disabled={loading}
                      className="btn btn-gradient w-full"
                    >
                      {loading ? (
                        <>
                          <svg className="animate-spin w-4 h-4" fill="none" viewBox="0 0 24 24">
                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                          </svg>
                          <span>Generating preview...</span>
                        </>
                      ) : (
                        <>
                          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.293a1 1 0 00-1.414 1.414L14.586 10l-1.293 1.293a1 1 0 101.414 1.414L16 11.414l1.293 1.293a1 1 0 001.414-1.414L17.414 10l1.293-1.293a1 1 0 00-1.414-1.414L16 8.586l-1.293-1.293z" clipRule="evenodd" />
                          </svg>
                          <span>Preview Data</span>
                        </>
                      )}
                    </button>
                    
                    <button
                      onClick={handleSchema}
                      disabled={loading}
                      className="btn btn-secondary w-full"
                    >
                      {loading ? (
                        <>
                          <svg className="animate-spin w-4 h-4" fill="none" viewBox="0 0 24 24">
                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                          </svg>
                          <span>Regenerating schema...</span>
                        </>
                      ) : (
                        <>
                          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clipRule="evenodd" />
                          </svg>
                          <span>Regenerate Schema</span>
                        </>
                      )}
                    </button>
                  </div>
                </div>
              </section>
            )}

            {/* Export Controls */}
            {preview.length > 0 && (
              <section className="card card-hover animate-slideUp">
                <div className="p-6">
                  <h2 className="text-lg font-semibold mb-4 flex items-center gap-2 text-theme">
                    <svg className="w-5 h-5 text-accent1" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 011.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clipRule="evenodd" />
                    </svg>
                    Export Options
                  </h2>
                  <RowSelector rows={rows} setRows={setRows} darkMode={darkMode} />
                  <GenerateButton columns={columns} rows={rows} darkMode={darkMode} />
                </div>
              </section>
            )}
          </div>

          {/* Right Column - Preview */}
          <div className="lg:col-span-2">
            <section className="card card-hover animate-slideUp">
              <div className="p-6">
                <h2 className="text-lg font-semibold mb-4 flex items-center gap-2 text-theme">
                  <svg className="w-5 h-5 text-accent1" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.293a1 1 0 00-1.414 1.414L14.586 10l-1.293 1.293a1 1 0 101.414 1.414L16 11.414l1.293 1.293a1 1 0 001.414-1.414L17.414 10l1.293-1.293a1 1 0 00-1.414-1.414L16 8.586l-1.293-1.293z" clipRule="evenodd" />
                  </svg>
                  Data Preview
                  {preview.length > 0 && (
                    <span className="ml-2 text-xs px-2 py-1 rounded-full bg-accent2 text-white">
                      {preview.length} rows
                    </span>
                  )}
                </h2>
                
                {preview.length === 0 ? (
                  <div className="text-center py-12">
                    <div className="w-20 h-20 mx-auto mb-4 rounded-full bg-surface flex items-center justify-center">
                      <svg className="w-10 h-10 text-accent2 opacity-60" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.293a1 1 0 00-1.414 1.414L14.586 10l-1.293 1.293a1 1 0 101.414 1.414L16 11.414l1.293 1.293a1 1 0 001.414-1.414L17.414 10l1.293-1.293a1 1 0 00-1.414-1.414L16 8.586l-1.293-1.293z" clipRule="evenodd" />
                      </svg>
                    </div>
                    <h3 className="text-xl font-semibold mb-2 text-theme">No data to preview</h3>
                    <p className="text-theme opacity-70">
                      Generate a schema and click "Preview Data" to see results
                    </p>
                  </div>
                ) : (
                  <PreviewTable data={preview} darkMode={darkMode} />
                )}
              </div>
            </section>
          </div>
        </div>
      </div>
      
      {/* Data Types Reference */}
      <DataTypesReference darkMode={darkMode} />
    </div>
  );
}
