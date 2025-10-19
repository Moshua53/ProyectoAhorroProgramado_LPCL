CREATE TABLE IF NOT EXISTS ahorros (
  id_ahorro SERIAL PRIMARY KEY,
  cedula VARCHAR(20) NOT NULL REFERENCES usuarios(cedula),
  meta NUMERIC(14,2) NOT NULL,
  meses INT NOT NULL CHECK (meses > 0),
  abonos_extras NUMERIC(14,2) DEFAULT 0,
  mes_abono_extra INT DEFAULT 0,
  interes NUMERIC(6,3) DEFAULT 0,
  ahorro_mensual NUMERIC(14,2) NOT NULL,
  objetivo VARCHAR(255)
);