// C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\frontend\src\pages\Services.js
import React, { useEffect, useState } from "react";
import api from "../Api";
import OrderModal from "../components/OrderModal";
import "./Services.css";

export default function Services(){
  const [sections, setSections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState({open:false, preset:null});

  useEffect(()=>{
    let ignore = false;
    api.get("/sections/").then(r=>{
      if(!ignore){ setSections(r.data?.results || r.data || []); setLoading(false); }
    }).catch(()=> setLoading(false));
    return ()=>{ ignore=true };
  },[]);

  return (
    <>
      <section className="container">
        <p className="section-sub">Мы закрываем полный цикл: анализ, дизайн, разработка и поддержка.</p>
        <h1 className="section-title">Наши услуги</h1>

        {loading && <div className="muted">Загружаем…</div>}

        {!loading && sections.length === 0 && (
          <div className="empty card">
            <div>
              <h3>Разделы услуг пока не добавлены</h3>
              <p className="muted">Зайдите в админку и создайте их: <code>/admin</code>.</p>
            </div>
            <button className="btn" onClick={()=>setModal({open:true, preset:"empty-services"})}>Оставить заявку</button>
          </div>
        )}

        <div className="grid cols-3 services-grid">
          {sections.map(s=>(
            <article className="service-card card" key={s.id}>
              <div className="icon">{s.icon?.slice(0,2) || "★"}</div>
              <h3>{s.title}</h3>
              <p className="muted">{s.content}</p>
              <div className="actions">
                <button className="btn" onClick={()=>setModal({open:true, preset:s.title})}>
                  Заказать
                </button>
              </div>
            </article>
          ))}
        </div>
      </section>

      <OrderModal open={modal.open} onClose={()=>setModal({open:false, preset:null})} preset={modal.preset}/>
    </>
  );
}
