import React from "react";
import { useOrderModal } from "../OrderModalContext";

export default function Home() {
  const { open } = useOrderModal();
  return (
    <section className="container" style={{padding: "24px 0"}}>
      <h1>IZOTOVLIFE — бизнес-сайт</h1>
      <p>Создаём сайты, автоматизируем процессы, подключаем аналитику.</p>
      <button className="btn" onClick={open}>Оставить заявку</button>
    </section>
  );
}
