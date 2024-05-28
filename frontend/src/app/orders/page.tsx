import Link from "next/link";
import OrderCard from "../components/orderCard";

async function getData() {
  const res = await fetch("http://127.0.0.1:8000/api/orders/");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return res.json();
}

export default async function Page() {
  const data = await getData();

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Orders</h1>
      <div className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {data.map((order) => (
          <OrderCard key={order.uuid} order={order} />
        ))}
      </div>
    </div>
  );
}
