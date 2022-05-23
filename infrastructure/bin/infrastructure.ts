#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";

import { context } from "../lib/contexts";
import { MainStack } from "../lib/main";

const app = new cdk.App({
  context,
});
new MainStack(app, "Automation/MainStack");
