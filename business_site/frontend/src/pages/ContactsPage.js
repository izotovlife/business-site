import React from "react";
import { useOrderModal } from "../OrderModalContext";

export default function ContactsPage() {
  const { open } = useOrderModal();
  return (
    <section className="container" style={{padding: "24px 0"}}>
      <h2>Контакты</h2>
      <p>Email: example@example.com</p>
      <p>Telegram: @yourhandle</p>
      <button className="btn" onClick={open}>Оставить заявку</button>
    </section>
  );
}
