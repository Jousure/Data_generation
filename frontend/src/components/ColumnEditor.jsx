export default function ColumnEditor({ columns, setColumns, darkMode }) {
  const addColumn = () => {
    setColumns([...columns, { name: "", type: "Text" }]);
  };

  const removeColumn = (index) => {
    setColumns(columns.filter((_, i) => i !== index));
  };

  const updateColumn = (index, field, value) => {
    const updated = [...columns];
    updated[index][field] = value;
    setColumns(updated);
  };

  // Comprehensive data types organized by category
  const dataTypes = [
    // Location & Address
    { group: "Location & Address", options: [
      "Address Line 2", "Airport Code", "Airport Continent", "Airport Country Code",
      "Airport Elevation (Feet)", "Airport GPS Code", "Airport Latitude", "Airport Longitude",
      "Airport Municipality", "Airport Name", "Airport Region Code", "City", "Country",
      "Country Code", "Latitude", "Longitude", "Postal Code", "State", "State (abbrev)",
      "Street Address", "Street Name", "Street Number", "Street Suffix", "Time Zone"
    ]},
    // Person & Demographics
    { group: "Person & Demographics", options: [
      "Animal Common Name", "Animal Scientific Name", "Family Name (Chinese)", "First Name",
      "First Name (European)", "First Name (Female)", "First Name (Male)", "Full Name",
      "Gender", "Gender (abbrev)", "Gender (Binary)", "Gender (Facebook)",
      "Given Name (Chinese)", "Job Title", "Race", "Title", "Username"
    ]},
    // Business & Finance
    { group: "Business & Finance", options: [
      "Bank City", "Bank Country Code", "Bank LEI", "Bank Name", "Bank RIAD Code",
      "Bank Routing Number", "Bank State", "Bank Street Address", "Bank SWIFT BIC",
      "Company Name", "Credit Card #", "Credit Card Type", "Currency", "Currency Code",
      "Department (Corporate)", "Department (Retail)", "DUNS Number", "EIN",
      "Fake Company Name", "Money", "Stock Industry", "Stock Market", "Stock Market Cap",
      "Stock Name", "Stock Sector", "Stock Symbol"
    ]},
    // Technology & Digital
    { group: "Technology & Digital", options: [
      "App Bundle ID", "App Name", "App Version", "Avatar", "Bitcoin Address",
      "Domain Name", "Ethereum Address", "IP Address v4", "IP Address v4 CIDR",
      "IP Address v6", "IP Address v6 CIDR", "MAC Address", "MD5", "MIME Type",
      "Mobile Device Brand", "Mobile Device Model", "Mobile Device OS", "Mobile Device Release Date",
      "SHA1", "SHA256", "Tezos Account", "Tezos Block", "Tezos Contract",
      "Tezos Operation", "Tezos Signature", "URL", "User Agent"
    ]},
    // Automotive
    { group: "Automotive", options: [
      "Car Make", "Car Model", "Car Model Year", "Car VIN"
    ]},
    // Healthcare & Medical
    { group: "Healthcare & Medical", options: [
      "Drug Company", "Drug Name (Brand)", "Drug Name (Generic)", "FDA NDC Code",
      "Hospital City", "Hospital Name", "Hospital NPI", "Hospital Postal Code",
      "Hospital State", "Hospital Street Address", "ICD10 Diagnosis Code", "ICD10 Dx Desc (Long)",
      "ICD10 Dx Desc (Short)", "ICD10 Proc Desc (Long)", "ICD10 Proc Desc (Short)",
      "ICD10 Procedure Code", "ICD9 Diagnosis Code", "ICD9 Dx Desc (Long)",
      "ICD9 Dx Desc (Short)", "ICD9 Proc Desc (Long)", "ICD9 Proc Desc (Short)",
      "ICD9 Procedure Code", "Medicare Beneficiary ID", "NHS Number"
    ]},
    // Construction
    { group: "Construction", options: [
      "Construction Heavy Equipment", "Construction Material", "Construction Role",
      "Construction Standard Cost Code", "Construction Subcontract Category", "Construction Trade"
    ]},
    // Entertainment & Media
    { group: "Entertainment & Media", options: [
      "Movie Genres", "Movie Title"
    ]},
    // Food & Grocery
    { group: "Food & Grocery", options: [
      "Product (Grocery)"
    ]},
    // Products & Retail
    { group: "Products & Retail", options: [
      "Product Category", "Product Description", "Product Name", "Product Price",
      "Product Subcategory", "Shirt Size"
    ]},
    // Identification Numbers
    { group: "Identification Numbers", options: [
      "GUID", "ISBN", "MongoDB ObjectID", "SSN", "ULID"
    ]},
    // Aviation
    { group: "Aviation", options: [
      "Flight Airline Code", "Flight Airline Name", "Flight Arrival Airport",
      "Flight Arrival Airport Code", "Flight Arrival City", "Flight Arrival Country",
      "Flight Departure Airport", "Flight Departure Airport Code", "Flight Departure City",
      "Flight Departure Country", "Flight Departure Time", "Flight Duration (Hours)",
      "Flight Number"
    ]},
    // Education
    { group: "Education", options: [
      "University"
    ]},
    // Professional Skills
    { group: "Professional Skills", options: [
      "LinkedIn Skill"
    ]},
    // Nature & Biology
    { group: "Nature & Biology", options: [
      "Plant Common Name", "Plant Family", "Plant Scientific Name"
    ]},
    // Data & Programming
    { group: "Data & Programming", options: [
      "Base64 Image URL", "Blank", "Boolean", "Character Sequence", "Color",
      "Custom List", "Dataset Column", "Digit Sequence", "Dummy Image URL",
      "Encrypt", "File Name", "Formula", "JSON Array", "Number",
      "Regular Expression", "Repeating Element", "Row Number", "Scenario",
      "Sequence", "SQL Expression", "Template", "Top Level Domain"
    ]},
    // Text & Content
    { group: "Text & Content", options: [
      "Buzzword", "Catch Phrase", "Email Address", "Frequency", "HCPCS Code",
      "HCPCS Name", "Hex Color", "Language", "Language Code", "Nato Phonetic",
      "Naughty String", "Paragraphs", "Password", "Password Hash",
      "Sentences", "Short Hex Color", "Slogan", "Words"
    ]},
    // Statistical Distributions
    { group: "Statistical Distributions", options: [
      "Binomial Distribution", "Exponential Distribution", "Geometric Distribution",
      "Normal Distribution", "Poisson Distribution"
    ]},
    // Dates & Times
    { group: "Dates & Times", options: [
      "Datetime", "Time"
    ]}
  ];

  return (
    <div className="space-y-3">
      {columns.map((col, i) => (
        <div key={i} className="flex items-center gap-2 p-3 bg-surface rounded-lg border border-theme theme-transition hover-glow">
          <input
            type="text"
            value={col.name}
            onChange={(e) => updateColumn(i, "name", e.target.value)}
            placeholder="Column name"
            className="input flex-1 text-sm"
          />
          <select
            value={col.type}
            onChange={(e) => updateColumn(i, "type", e.target.value)}
            className="input text-sm min-w-48"
          >
            <option value="">Select data type...</option>
            {dataTypes.map((group) => (
              <optgroup key={group.group} label={group.group}>
                {group.options.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
          <button
            onClick={() => removeColumn(i)}
            className="p-2 rounded-lg bg-red-100 text-red-600 hover:bg-red-200 theme-transition"
          >
            <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
          </button>
        </div>
      ))}
      
      <button
        onClick={addColumn}
        className="btn btn-secondary w-full"
      >
        <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path fillRule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clipRule="evenodd" />
        </svg>
        Add Column
      </button>
    </div>
  );
}
