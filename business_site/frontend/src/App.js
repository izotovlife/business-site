// C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\frontend\src\App.js
import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Services from "./pages/Services";
import Portfolio from "./pages/Portfolio";
import Testimonials from "./pages/Testimonials";
import "./theme.css";

export default function App(){
  return (
    <BrowserRouter>
      <Header/>
      <main>
        <Routes>
          <Route path="/" element={<Navigate to="/services" replace/>}/>
          <Route path="/services" element={<Services/>}/>
          <Route path="/portfolio" element={<Portfolio/>}/>
          <Route path="/testimonials" element={<Testimonials/>}/>
          <Route path="*" element={<div className="container">Страница не найдена</div>} />
        </Routes>
      </main>
      <Footer/>
    </BrowserRouter>
  );
}
