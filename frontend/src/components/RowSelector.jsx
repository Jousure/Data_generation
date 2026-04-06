export default function RowSelector({ rows, setRows, darkMode }) {
  return (
    <div className="space-y-3">
      <label className={`block text-sm font-semibold ${
        darkMode ? 'text-primary-200' : 'text-primary-700'
      }`}>
        Number of rows to generate
      </label>
      <select
        value={rows}
        onChange={(e) => setRows(Number(e.target.value))}
        className={`w-full px-4 py-3 border-2 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all duration-200 font-sans ${
          darkMode 
            ? 'bg-primary-700 border-primary-600 text-white' 
            : 'bg-white border-primary-200 text-primary-900'
        }`}
      >
        <option value={100}>100 rows</option>
        <option value={1000}>1,000 rows</option>
        <option value={10000}>10,000 rows</option>
        <option value={100000}>100,000 rows</option>
        <option value={1000000}>1,000,000 rows</option>
      </select>
    </div>
  );
}
