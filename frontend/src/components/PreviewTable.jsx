export default function PreviewTable({ data, darkMode }) {
  if (!data.length) return null;

  const cols = Object.keys(data[0]);

  return (
    <div className="overflow-x-auto">
      <div className="inline-block min-w-full align-middle">
        <div className={`overflow-hidden rounded-xl border shadow-sm ${
          darkMode ? 'border-primary-600' : 'border-primary-200'
        }`}>
          <table className="min-w-full divide-y">
            <thead className={darkMode ? 'bg-primary-700' : 'bg-primary-50'}>
              <tr>
                {cols.map(c => (
                  <th key={c} className={`px-6 py-3 text-left text-xs font-semibold uppercase tracking-wider ${
                    darkMode 
                      ? 'text-primary-300 border-primary-600' 
                      : 'text-primary-700 border-primary-200'
                  } border-b`}>
                    {c}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className={`divide-y ${
              darkMode ? 'divide-primary-700 bg-primary-800' : 'divide-primary-200 bg-white'
            }`}>
              {data.slice(0, 10).map((row, i) => (
                <tr key={i} className={darkMode ? 'hover:bg-primary-700' : 'hover:bg-primary-50'}>
                  {cols.map(c => (
                    <td key={c} className={`px-6 py-4 whitespace-nowrap text-sm font-medium ${
                      darkMode ? 'text-primary-200' : 'text-primary-900'
                    }`}>
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
          <div className={`text-center mt-4 text-sm font-medium ${
            darkMode ? 'text-primary-400' : 'text-primary-600'
          }`}>
            Showing 10 of {data.length.toLocaleString()} rows
          </div>
        )}
      </div>
    </div>
  );
}
