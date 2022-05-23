import * as cdk from "aws-cdk-lib";

import * as ssm from "aws-cdk-lib/aws-ssm";

import { getSsmContext } from "../contexts";

type Props = {};

export const createSSM = (stack: cdk.Stack, props: Props) => {
  createParameters(stack, {});
  return;
};

type ParameterStoreProps = {};
const createParameters = (stack: cdk.Stack, props: ParameterStoreProps) => {
  const { confluence } = getSsmContext(stack);
  new ssm.StringParameter(stack, "ConfluenceUrlParameterStore", {
    allowedPattern: ".*",
    description: "Confluence URL",
    parameterName: "/automation/confluence/URL",
    stringValue: confluence.url,
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceUserParameterStore", {
    allowedPattern: ".*",
    description: "Confluence User",
    parameterName: "/automation/confluence/USER",
    stringValue: confluence.user,
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceTokenParameterStore", {
    allowedPattern: ".*",
    description: "Confluence Token",
    parameterName: "/automation/confluence/TOKEN",
    stringValue: confluence.token,
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceSpaceParameterStore", {
    allowedPattern: ".*",
    description: "Confluence Space",
    parameterName: "/automation/confluence/SPACE",
    stringValue: confluence.space,
    tier: ssm.ParameterTier.STANDARD,
  });
  new ssm.StringParameter(stack, "ConfluenceParentPageParameterStore", {
    allowedPattern: ".*",
    description: "Confluence Parent Page",
    parameterName: "/automation/confluence/PARENT_PAGE",
    stringValue: confluence.parentPage,
    tier: ssm.ParameterTier.STANDARD,
  });
};
