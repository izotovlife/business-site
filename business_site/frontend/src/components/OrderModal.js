// C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\frontend\src\components\OrderModal.js
import React, { useState } from "react";
import api from "../Api";
import "./OrderModal.css";

export default function OrderModal({open, onClose, preset}){
  const [form, setForm] = useState({ name:"", contact:"", message:"" });
  const [status, setStatus] = useState(null);

  if(!open) return null;

  const submit = async (e)=>{
    e.preventDefault();
    setStatus("loading");
    try{
      await api.post("/leads/", {...form, source: preset || "site"});
      setStatus("ok");
      setForm({name:"", contact:"", message:""});
      setTimeout(onClose, 900);
    }catch(err){
      setStatus("err");
    }
  };

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal" onClick={(e)=>e.stopPropagation()}>
        <h3>Оставить заявку</h3>
        <form onSubmit={submit} className="modal-form">
          <input required placeholder="Ваше имя"
                 value={form.name} onChange={e=>setForm({...form, name:e.target.value})}/>
          <input required placeholder="Телефон, email или Telegram"
                 value={form.contact} onChange={e=>setForm({...form, contact:e.target.value})}/>
          <textarea rows={4} placeholder="Кратко опишите задачу"
                    value={form.message} onChange={e=>setForm({...form, message:e.target.value})}/>
          <button className="btn" type="submit" disabled={status==="loading"}>
            {status==="loading" ? "Отправляем..." : "Отправить"}
          </button>
          {status==="ok"  && <div className="hint ok">Готово! Свяжемся с вами.</div>}
          {status==="err" && <div className="hint err">Ошибка. Попробуйте ещё раз.</div>}
        </form>
        <button className="modal-close" onClick={onClose} aria-label="Закрыть">×</button>
      </div>
    </div>
  );
}
