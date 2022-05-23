import { ssmContext } from "./ssm";

export { useContext } from "./common";
export { getSsmContext } from "./ssm";

export const context = {
  ...ssmContext,
};
