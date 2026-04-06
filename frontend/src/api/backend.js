const BASE_URL = "http://127.0.0.1:8000";

export async function getSchema(prompt) {
  const res = await fetch(`${BASE_URL}/schema`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  if (!res.ok) throw new Error("Failed to generate schema");
  return res.json();
}

export async function getPreview(columns) {
  const res = await fetch(`${BASE_URL}/preview`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ columns }),
  });
  if (!res.ok) throw new Error("Failed to generate preview");
  return res.json();
}

export async function generateCSV(columns, rows) {
  const res = await fetch(`${BASE_URL}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ columns, rows }),
  });
  if (!res.ok) throw new Error("Failed to generate CSV");
  return res.json();
}
