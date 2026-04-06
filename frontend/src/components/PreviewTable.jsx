export default function PreviewTable({ data, darkMode }) {
  if (!data.length) return null;

  const cols = Object.keys(data[0]);

  return (
    <div className="overflow-x-auto">
      <div className="inline-block min-w-full align-middle">
        <div className="card overflow-hidden">
          <table className="min-w-full divide-y">
            <thead className="bg-surface">
              <tr>
                {cols.map(c => (
                  <th key={c} className={`px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider text-theme border-b border-theme`}>
                    {c}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className={`divide-y divide-theme`}>
              {data.slice(0, 10).map((row, i) => (
                <tr key={i} className="hover:bg-accent1 hover:bg-opacity-10 theme-transition">
                  {cols.map(c => (
                    <td key={c} className={`px-6 py-4 whitespace-nowrap text-sm font-medium text-theme`}>
                      <div className="max-w-xs truncate" title={String(row[c])}>
                        {String(row[c])}
                      </div>
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {data.length > 10 && (
          <div className="text-center mt-4 text-sm font-medium text-accent2">
            Showing 10 of {data.length.toLocaleString()} rows
          </div>
        )}
      </div>
    </div>
  );
}
