"use client";

import Link from "next/link";

interface CustomerCardProps {
  customer: {
    uuid: string;
    name: string;
    email: string;
    phone: string;
  };
}

const CustomerCard = ({ customer }) => {
  return (
    <div className="border p-4 rounded shadow-md mb-4 max-w-[600px]">
      <div>Customer: {customer.name}</div>
      <div>Email: ${customer.email}</div>
      <div>phone: {customer.phone}</div>
    </div>
  );
};

export default CustomerCard;
