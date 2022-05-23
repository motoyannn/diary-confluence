import * as dotenv from "dotenv";

import { useContext } from "./common";

dotenv.config();

/** SSM */
export const [ssmContext, getSsmContext] = useContext<{
  confluence: {
    url: string;
    user: string;
    token: string;
    space: string;
    parentPage: string;
  };
}>({
  key: "ssm",
  value: {
    confluence: {
      url: process.env.CONFLUENCE_URL || "",
      user: process.env.CONFLUENCE_USER || "",
      token: process.env.CONFLUENCE_TOKEN || "",
      space: process.env.CONFLUENCE_SPACE || "",
      parentPage: process.env.CONFLUENCE_PARENT_PAGE || "",
    },
  },
});
