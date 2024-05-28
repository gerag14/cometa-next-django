import Link from "next/link";

export default function Page() {
  return (
    <h1 className="text-3xl font-bold underline">
      Hello world!
      <Link href="/orders">Orders</Link>
    </h1>
  );
}
