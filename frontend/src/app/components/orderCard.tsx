"use client";

import { useState } from "react";
import Link from "next/link";
import OrderCardDetail from "./orderCardDetail";

const OrderCard = ({ order }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="border p-4 rounded shadow-md mb-4 max-w-[600px]">
      <div className="mb-2">
        <Link
          href={`/orders/${order.uuid}`}
          className="text-blue-500 hover:underline"
        >
          Order ID {order.uuid}
        </Link>
      </div>
      <div>Order Date: {order.created_on}</div>
      <div>Customer: {order.customer_email}</div>
      <div>Total: ${order.total}</div>
      <div>Status: {order.status}</div>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="text-white bg-emerald-600 px-4 py-2 rounded-md mt-4"
      >
        {isOpen ? "Ver menos" : "Ver más"}
      </button>
      {isOpen && <OrderCardDetail items={order.items} />}
    </div>
  );
};

export default OrderCard;
