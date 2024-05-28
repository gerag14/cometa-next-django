import OrderCard from "../../components/orderCard";

async function getData(order: string) {
  const res = await fetch("http://127.0.0.1:8000/api/orders/" + order + "/");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function Page({ params }: { params: { order: string } }) {
  const order_data = await getData(params.order);

  return (
    <div>
      <h1 className="text-2xl font-bold">Orders</h1>
      <button className="bg-blue-500 text-white px-4 py-2 rounded-md">
        Create new Order
      </button>
      <OrderCard order={order_data} />
    </div>
  );
}
