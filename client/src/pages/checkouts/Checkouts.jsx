import React, { useState } from "react";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";
import { useTransition } from "@react-spring/web";
import { animated } from "@react-spring/web";
import { Link } from "react-router-dom";
import "../../App.scss";

export const Checkouts = () => {
  const [showNavbar, setShowNavbar] = useState(false);
  const transition = useTransition(showNavbar, {
    from: { x: -100, y: 100, opacity: 0 },
    enter: { x: 0, y: 0, opacity: 1 },
    leave: { x: 100, y: 100, opacity: 0 },
  });
  return (
    <div className="revenue_wrapper">
      <div className="nav_container">
        <div className="drop_down">
          <span style={{ marginTop: "1%", flex: "0 0 53%" }}>
            Запросы на выплату
          </span>
          <div
            className="drop_down_button"
            onClick={() => setShowNavbar((prev) => !prev)}
          >
            {showNavbar ? (
              <CloseIcon fontSize="large" />
            ) : (
              <MenuIcon fontSize="large" />
            )}
          </div>
        </div>
        {transition((style, item) =>
          item ? (
            <animated.div style={style} className="rev_buttons">
              <Link
                to={"/revenue"}
                style={{
                  width: "100%",
                  height: "100%",
                  display: "flex",
                  justifyContent: "center",
                  textDecoration: "none",
                  color: "var(--tg-theme-button-text-color)",
                }}
              >
                <animated.button style={style}>Доходность</animated.button>
              </Link>
            </animated.div>
          ) : (
            ""
          )
        )}
      </div>
      <div className="revenue_container">
        <div style={{ width: "100%", height: "100%" }}>
          <table border="2" className="checkouts_table">
            <tbody>
              <tr>
                <td>Дата создания запроса</td>
                <td>Сумма вывода</td>
                <td>Статус запроса</td>
              </tr>
              <tr>
                <td>28/9/2023</td>
                <td>1800 ₽</td>
                <td>Обработан</td>
              </tr>
              <tr>
                <td>27/9/2023</td>
                <td>1800 ₽</td>
                <td>В обработке</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
