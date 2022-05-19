import * as cdk from "aws-cdk-lib";

import { createSSM } from "./modules";

type Props = {} & cdk.StackProps;

export class MainStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: Props) {
    super(scope, id, props);

    const ssm = createSSM(this, {});
  }
}
