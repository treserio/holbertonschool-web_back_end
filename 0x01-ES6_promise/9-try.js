export default function guardrail(mathfunction) {
  try {
    return [mathfunction(), 'Guardrail was processed']
  } catch (err) {
    return [err, 'Guardrail was processed']
  }
}
