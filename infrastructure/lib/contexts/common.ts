import * as cdk from "aws-cdk-lib";

type CreateContext<T> = {
  key: string;
  value?: T;
  validate?: (context: T) => boolean;
};
export function useContext<T>(
  context: CreateContext<T>
): [{ [key: string]: string }, (scope: cdk.Stack | cdk.App) => T] {
  const { key, value, validate } = context;

  return [
    { [key]: value ? JSON.stringify(value) : "" },
    (scope) => {
      const context = scope.node.tryGetContext(key);
      if (!context) throw new Error(`${key} does not exists.`);
      try {
        const contextObj = JSON.parse(scope.node.tryGetContext(key)) as T;
        if (validate) validate(contextObj);
        return contextObj;
      } catch (e) {
        /** JSON のパースに失敗した場合はリテラルとして処理する */
        if (e instanceof SyntaxError) {
          if (validate) validate(context);
          return context;
        } else {
          throw e;
        }
      }
    },
  ];
}
