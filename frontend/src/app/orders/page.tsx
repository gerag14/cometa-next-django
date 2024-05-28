"use client";

import OrderCard from "../components/orderCard";
import useOrdersData from "../hooks/useOrdersData";

export default function Page() {
  const { orders, loading, error } = useOrdersData();

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Orders</h1>
        <button className="bg-blue-500 text-white px-4 py-2 rounded-md">
          Create new Order
        </button>
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {orders.map((order) => (
          <OrderCard key={order.uuid} order={order} />
        ))}
      </div>
    </div>
  );
}
