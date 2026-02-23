export default function RowSelector({ rows, setRows }) {
  return (
    <div className="mb-6">
      <label className="block font-semibold mb-2">
        Number of rows
      </label>
      <select
        value={rows}
        onChange={(e) => setRows(Number(e.target.value))}
        className="border p-2 rounded"
      >
        <option value={100}>100</option>
        <option value={1000}>1,000</option>
        <option value={10000}>10,000</option>
        <option value={100000}>100,000</option>
        <option value={1000000}>1,000,000</option>
      </select>
    </div>
  );
}
