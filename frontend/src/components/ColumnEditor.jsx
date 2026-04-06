export default function ColumnEditor({ columns, setColumns, darkMode }) {
  function remove(col) {
    setColumns(columns.filter(c => c !== col));
  }

  function add() {
    const name = prompt("New column name");
    if (name && name.trim()) {
      setColumns([...columns, name.trim()]);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap gap-2">
        {columns.map(col => (
          <span
            key={col}
            onClick={() => remove(col)}
            className={`px-3 py-2 rounded-lg cursor-pointer transition-all duration-200 flex items-center gap-2 font-medium text-sm ${
              darkMode 
                ? 'bg-primary-700 hover:bg-red-900/50 text-white hover:shadow-md' 
                : 'bg-primary-100 hover:bg-red-100 text-primary-800 hover:shadow-md'
            }`}
          >
            <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
            {col}
          </span>
        ))}
      </div>
      <button
        onClick={add}
        className={`px-4 py-2 rounded-xl font-medium transition-all duration-200 flex items-center gap-2 ${
          darkMode 
            ? 'bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700 text-white shadow-lg hover:shadow-xl' 
            : 'bg-gradient-to-r from-primary-500 to-primary-600 hover:from-primary-600 hover:to-primary-700 text-primary-900 shadow-lg hover:shadow-xl'
        }`}
      >
        <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clipRule="evenodd" />
        </svg>
        Add Column
      </button>
    </div>
  );
}
