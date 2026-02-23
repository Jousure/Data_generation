export default function ColumnEditor({ columns, setColumns }) {
  function remove(col) {
    setColumns(columns.filter(c => c !== col));
  }

  function add() {
    const name = prompt("New column name");
    if (name) setColumns([...columns, name]);
  }

  return (
    <div className="mb-6">
      <h3 className="font-semibold mb-2">Columns</h3>
      <div className="flex flex-wrap gap-2">
        {columns.map(col => (
          <span
            key={col}
            onClick={() => remove(col)}
            className="px-3 py-1 bg-gray-200 rounded cursor-pointer hover:bg-red-200"
          >
            {col} ✕
          </span>
        ))}
      </div>
      <button
        onClick={add}
        className="mt-3 px-3 py-1 bg-green-600 text-white rounded"
      >
        Add Column
      </button>
    </div>
  );
}
