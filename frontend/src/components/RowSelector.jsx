export default function RowSelector({ rows, setRows, darkMode }) {
  return (
    <div className="space-y-3">
      <label className={`block text-sm font-semibold text-theme theme-transition`}>
        Number of rows to generate
      </label>
      <select
        value={rows}
        onChange={(e) => setRows(Number(e.target.value))}
        className="input"
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
