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
      <h1>Order {order_data.uuid}</h1>
      <OrderCard order={order_data} />
    </div>
  );
}
