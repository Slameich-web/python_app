import React, { useState, useEffect } from "react";
import { $api } from "../../http/index";
import "../../App.scss";
import { useNavigate } from "react-router-dom";

export const Register = () => {
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [isRedirect, setIsEedirect] = useState(false);
  const isShowPassword = showPassword ? "text" : "password";
  const navigate = useNavigate();

  const registerRequest = async () => {
    try {
      await $api.post("/api/register", {
        email: email,
        password: password,
        telegram_id: 5421,
      });
      setIsEedirect(true);
    } catch (e) {
      setError(e?.response?.data?.message);
    }
  };

  useEffect(() => {
    if (isRedirect) {
      return navigate("/login");
    }
  }, [isRedirect, navigate]);

  return (
    <div className="auth_wrapper">
      <div className="auth_container">
        <form className="input_container">
          <input
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            type="email"
          />
          <input
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Пароль"
            type={isShowPassword}
          />
        </form>
        <div>
          <span>Показать пароль </span>
          <input
            type="checkbox"
            onChange={() => setShowPassword((prev) => !prev)}
          />
        </div>
        <button onClick={registerRequest} className="login_button">
          Регистрация
        </button>
        <div>{error}</div>
      </div>
    </div>
  );
};
