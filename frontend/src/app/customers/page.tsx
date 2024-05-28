import CustomerCard from "../components/customerCard";
async function getData() {
  const res = await fetch("http://127.0.0.1:8000/api/customers/");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return res.json();
}

export default async function Page() {
  const data = await getData();

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Customers</h1>
        <button className="bg-blue-500 text-white px-4 py-2 rounded-md">
          Create Customer
        </button>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {data.map((customer) => (
          <CustomerCard key={customer.uuid} customer={customer} />
        ))}
      </div>
    </div>
  );
}
