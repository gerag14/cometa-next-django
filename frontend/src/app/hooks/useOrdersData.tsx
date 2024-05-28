"use client";

import { useEffect, useState } from "react";
import useFetchData from "./useFetchData";

export interface OrderItem {
  uuid: string;
  product_name: string;
  quantity: number;
  price: string;
}

export interface Order {
  uuid: string;
  created_on: string;
  status: string;
  total: string;
  customer_email: string;
  items: OrderItem[];
}

export interface OrderCardProps {
  order: Order;
}

const useOrdersData = () => {
  const { data, loading, error } = useFetchData(
    "http://127.0.0.1:8000/api/orders/"
  );
  const [orders, setOrders] = useState<Order[]>([]);

  useEffect(() => {
    if (data) {
      setOrders(data);
    }
  }, [data]);

  return { orders, loading, error };
};

export default useOrdersData;
