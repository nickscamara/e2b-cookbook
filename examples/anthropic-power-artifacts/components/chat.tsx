import { Terminal } from 'lucide-react'
import { Message } from 'ai/react'
import { Input } from '@/components/ui/input'

export interface Props {
  messages: Message[],
  input: string,
  handleInputChange: (e: React.ChangeEvent<HTMLInputElement>) => void,
  handleSubmit: (e: React.FormEvent<HTMLFormElement>) => void,
}

export function Chat({
  messages,
  input,
  handleInputChange,
  handleSubmit,
}: Props) {
  console.log('messages', messages)

  return (
    <div className="flex-1 flex flex-col py-4 gap-4 max-h-full justify-between">
      <div className="flex flex-col gap-2 overflow-y-auto max-h-full px-4 rounded-lg">
        {messages.map(message => (
          <div className={`py-2 px-4 shadow-sm whitespace-pre-wrap ${message.role !== 'user' ? 'bg-white' : 'bg-white/40'} rounded-lg border-b border-[#FFE7CC] font-serif`} key={message.id}>
            {message.content}
            {message.toolInvocations && message.toolInvocations.length > 0 &&
              <div className="mt-4 flex justify-start items-start border border-[#FFE7CC] rounded-md">
                <div className="p-2 self-stretch border-r border-[#FFE7CC] bg-[#FFE7CC] w-14 flex items-center justify-center">
                  <Terminal strokeWidth={2} className="text-[#FF8800]"/>
                </div>
                <div className="p-2 flex flex-col space-y-1 justify-start items-start min-w-[100px]">
                  {message.toolInvocations[0].toolName === "runPython" &&
                    <>
                      <span className="font-bold font-sans text-sm">{message.toolInvocations[0].args.title}</span>
                      <span className="font-sans text-sm">{message.toolInvocations[0].args.description}</span>
                    </>
                  }
                </div>
              </div>
            }
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit}>
        <Input placeholder="Ask Claude..." value={input} onChange={handleInputChange}/>
      </form>
    </div>
  )
}