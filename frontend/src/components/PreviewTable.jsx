export default function PreviewTable({ data }) {
  if (!data.length) return null;

  const cols = Object.keys(data[0]);

  return (
    <div className="overflow-x-auto mb-6">
      <table className="min-w-full border">
        <thead className="bg-gray-100">
          <tr>
            {cols.map(c => (
              <th key={c} className="p-2 border">{c}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              {cols.map(c => (
                <td key={c} className="p-2 border">
                  {String(row[c])}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
