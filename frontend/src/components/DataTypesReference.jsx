import { useState, useEffect } from 'react';
import { getDataTypes } from '../api/backend';

export default function DataTypesReference({ darkMode }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeCategory, setActiveCategory] = useState('all');
  const [dataTypes, setDataTypes] = useState({ categories: {}, allTypes: [] });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchDataTypes() {
      try {
        const response = await getDataTypes();
        if (response.success) {
          setDataTypes(response.data);
        }
      } catch (error) {
        console.error('Failed to fetch data types:', error);
      } finally {
        setLoading(false);
      }
    }
    
    if (isOpen && dataTypes.allTypes.length === 0) {
      fetchDataTypes();
    }
  }, [isOpen, dataTypes.allTypes.length]);

  const categories = [
    { id: 'all', name: 'All Types', icon: '📋' },
    ...Object.keys(dataTypes.categories).map(catName => ({
      id: catName.toLowerCase().replace(/[^a-z0-9]/g, '-'),
      name: catName,
      icon: getCategoryIcon(catName)
    }))
  ];

  function getCategoryIcon(category) {
    const icons = {
      'Location & Address': '📍',
      'Person & Demographics': '👤',
      'Business & Finance': '💼',
      'Technology & Digital': '💻',
      'Automotive': '🚗',
      'Healthcare & Medical': '🏥',
      'Construction': '🏗️',
      'Entertainment & Media': '🎬',
      'Products & Retail': '🛍️',
      'Identification Numbers': '🆔',
      'Aviation': '✈️',
      'Education': '🎓',
      'Nature & Biology': '🌿',
      'Data & Programming': '💾',
      'Text & Content': '📝',
      'Statistical Distributions': '📊',
      'Dates & Times': '📅'
    };
    return icons[category] || '📋';
  }

  const getFilteredTypes = () => {
    if (activeCategory === 'all') return dataTypes.allTypes;
    
    const categoryKey = Object.keys(dataTypes.categories).find(
      cat => cat.toLowerCase().replace(/[^a-z0-9]/g, '-') === activeCategory
    );
    
    return categoryKey ? dataTypes.categories[categoryKey] : [];
  };

  if (loading && isOpen) {
    return (
      <div className="fixed bottom-4 right-4 z-50">
        <button
          onClick={() => setIsOpen(false)}
          className={`px-4 py-3 rounded-full shadow-lg transition-all duration-300 flex items-center gap-2 theme-transition ${
            darkMode 
              ? 'bg-gradient-to-r from-theme-accent1 to-theme-accent2 text-theme' 
              : 'bg-gradient-to-r from-theme-button to-theme-accent2 text-theme'
          }`}
        >
          <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin"></div>
          <span className="font-medium">Loading...</span>
        </button>
      </div>
    );
  }

  return (
    <div className="fixed bottom-4 right-4 z-50">
      {/* Toggle Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`px-4 py-3 rounded-full shadow-lg transition-all duration-300 flex items-center gap-2 theme-transition ${
          darkMode 
            ? 'bg-gradient-to-r from-theme-accent1 to-theme-accent2 text-theme hover:from-theme-accent2 hover:to-theme-hover' 
            : 'bg-gradient-to-r from-theme-button to-theme-accent2 text-theme hover:from-theme-accent1 hover:to-theme-button'
        }`}
      >
        <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clipRule="evenodd" />
        </svg>
        <span className="font-medium">Data Types</span>
        {isOpen && (
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
          </svg>
        )}
      </button>

      {/* Reference Panel */}
      {isOpen && (
        <div className={`absolute bottom-16 right-0 w-96 max-h-96 rounded-2xl shadow-2xl border overflow-hidden theme-transition ${
          darkMode 
            ? 'bg-primary-800 border-theme-accent2/30' 
            : 'bg-primary-50 border-theme-accent1/30'
        }`}>
          <div className="p-4">
            <h3 className={`text-lg font-semibold mb-4 text-theme`}>
              Available Data Types ({dataTypes.total_count || 0})
            </h3>
            
            {/* Category Tabs */}
            <div className="flex flex-wrap gap-2 mb-4 max-h-20 overflow-y-auto">
              {categories.map(category => (
                <button
                  key={category.id}
                  onClick={() => setActiveCategory(category.id)}
                  className={`px-3 py-1 rounded-full text-xs font-medium transition-all duration-200 theme-transition ${
                    activeCategory === category.id
                      ? darkMode 
                        ? 'bg-theme-accent1 text-theme' 
                        : 'bg-theme-accent2 text-theme'
                      : darkMode
                        ? 'bg-primary-700 text-theme hover:bg-primary-600'
                        : 'bg-primary-200 text-theme hover:bg-primary-300'
                  }`}
                >
                  <span className="mr-1">{category.icon}</span>
                  {category.name}
                </button>
              ))}
            </div>

            {/* Data Types List */}
            <div className="max-h-48 overflow-y-auto space-y-2">
              {getFilteredTypes().map(type => (
                <div
                  key={type}
                  className={`px-3 py-2 rounded-lg text-sm font-medium cursor-pointer transition-all duration-200 theme-transition ${
                    darkMode
                      ? 'bg-primary-700 hover:bg-primary-600 text-theme'
                      : 'bg-primary-200 hover:bg-primary-300 text-theme'
                  }`}
                  onClick={() => {
                    navigator.clipboard.writeText(type);
                    // You could add a toast notification here
                  }}
                  title="Click to copy"
                >
                  {type}
                </div>
              ))}
            </div>

            {/* Usage Tips */}
            <div className={`mt-4 p-3 rounded-lg text-xs ${
              darkMode ? 'bg-primary-700 text-theme' : 'bg-primary-200 text-theme'
            }`}>
              <p className="font-medium mb-1">💡 Usage Tips:</p>
              <ul className="space-y-1 opacity-80">
                <li>• Click any data type to copy it</li>
                <li>• Use natural language in descriptions</li>
                <li>• Combine multiple types for complex datasets</li>
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
