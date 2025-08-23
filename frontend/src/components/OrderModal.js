import React, { useEffect, useState } from "react";
import api from "../Api";
import "./OrderModal.css";

export default function OrderModal({ open, onClose, preset, serviceId }) {
  const [services, setServices] = useState([]);
  const [form, setForm] = useState({
    name: "",
    phone: "",
    email: "",
    service: serviceId || "",
    message: "",
    consent: false,
    company: "",
  });
  const [status, setStatus] = useState(null);

  useEffect(() => {
    if (open) {
      api.get("/services/").then((res) => setServices(res.data));
      setForm((f) => ({ ...f, service: serviceId || "" }));
      setStatus(null);
    }
  }, [open, serviceId]);

  if (!open) return null;

  const submit = async (e) => {
    e.preventDefault();
    if (form.company) return; // honeypot
    setStatus("loading");
    try {
      await api.post(`/leads/?src=${preset || "site"}`, {
        name: form.name,
        phone: form.phone,
        email: form.email,
        service: form.service || null,
        message: form.message,
        consent: form.consent,
      });
      setStatus("ok");
      setForm({
        name: "",
        phone: "",
        email: "",
        service: "",
        message: "",
        consent: false,
        company: "",
      });
      setTimeout(() => {
        onClose();
        setStatus(null);
      }, 1000);
    } catch (err) {
      setStatus("err");
    }
  };

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <h3>Оставить заявку</h3>
        <form onSubmit={submit} className="modal-form">
          <input
            placeholder="Ваше имя"
            value={form.name}
            onChange={(e) => setForm({ ...form, name: e.target.value })}
          />
          <input
            placeholder="Телефон"
            value={form.phone}
            onChange={(e) => setForm({ ...form, phone: e.target.value })}
          />
          <input
            placeholder="Email"
            value={form.email}
            onChange={(e) => setForm({ ...form, email: e.target.value })}
          />
          <select
            value={form.service}
            onChange={(e) => setForm({ ...form, service: e.target.value })}
          >
            <option value="">Выберите услугу</option>
            {services.map((s) => (
              <option key={s.id} value={s.id}>
                {s.title}
              </option>
            ))}
          </select>
          <textarea
            rows={4}
            placeholder="Сообщение"
            value={form.message}
            onChange={(e) => setForm({ ...form, message: e.target.value })}
          />
          <label className="consent">
            <input
              type="checkbox"
              checked={form.consent}
              onChange={(e) => setForm({ ...form, consent: e.target.checked })}
            />{" "}
            Согласен на обработку данных
          </label>
          <input
            style={{ display: "none" }}
            value={form.company}
            onChange={(e) => setForm({ ...form, company: e.target.value })}
          />
          <button className="btn" type="submit" disabled={status === "loading"}>
            {status === "loading" ? "Отправляем..." : "Отправить"}
          </button>
          {status === "ok" && <div className="hint ok">Заявка отправлена</div>}
          {status === "err" && <div className="hint err">Ошибка отправки</div>}
        </form>
        <button className="modal-close" onClick={onClose} aria-label="Закрыть">
          ×
        </button>
      </div>
    </div>
  );
}
